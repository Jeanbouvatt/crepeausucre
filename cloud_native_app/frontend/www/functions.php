<?php

if(!isset($_GET['id'])) {
  die("Veuillez renseigner un paramètre id dans l'url.");
}

$url = "http://0.0.0.0";
$id = $_GET['id'];

if (isset($_GET['play'])) {
  if(!autenticate()) {
    echo "Vous n'êtes pas identifié.";
  }
  elseif(!check_played()) {
    echo "Vous avez déjà joué.";
  }
  else {
    $r = get(play_link());
    $result = json_decode($r);
    update_price($result->price);
    update_played();
  }
}

function check_played() {
  global $url, $id;
  $code = get_code($url . ':8092/get_status/' . $id);
  return $code == 200;
}

function autenticate() {
  global $url, $id;
  $code = get_code($url . ':8091/login/' . $id);
  return $code == 200;
}

function play_link() {
  global $url, $id;
  $r = get($url . ':8093/get_button/' . $id);
  $result = json_decode($r);
  if ($result->msg == "ok") {
    return $result->html;
  }
  else {
    throw new Exception("Impossible de récupérer le lien pour jouer.");
  }

}

function get_price() {
  global $url, $id;
  $r = get($url . ':8094/get_price/' . $id);
  $result = json_decode($r);
  return $result->msg;
}

function update_played() {
  global $url, $id;
  $code = get($url . ':8092/set_status/' . $id);
}

function update_price($price_name) {
  global $url, $id;
  $code = get_code($url . ':8094/set_price/' . $id . '/' . $price_name);
}

function get($url) {
  $r = curl_init();

  curl_setopt($r, CURLOPT_URL, $url);
  curl_setopt($r, CURLOPT_RETURNTRANSFER, true);

  $res = curl_exec($r);
  curl_close($r);

  return $res;
}

function get_code($url) {
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_HEADER, true);    // we want headers
  curl_setopt($ch, CURLOPT_NOBODY, true);    // we don't need body
  curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);
  $output = curl_exec($ch);
  $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  curl_close($ch);

  return $httpcode;
}

<?php

class Curl {

  public function get($url) {
    $r = curl_init();

    curl_setopt($r, CURLOPT_URL, $url);
    curl_setopt($r, CURLOPT_GET, true);

    $res = curl_exec($r);
    curl_close();

    return $res;
  }

}

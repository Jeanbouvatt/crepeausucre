<?php 

class Urls {
  private $confFileName = "conf";

  private $compulsory = array("i", "p", "s", "b");

  private static $instance = null;

  public static function get_instance() {
    if(self::$instance == NULL) {
      self::$instance = new Urls();
    }
    return self::$instance;
  }

  private function __construct() {
    $conf_array = parse_ini_file($this->confFileName);
    $diff = array_diff($this->compulsory, array_keys($conf_array));
    if($diff != []) {
      die("Des adresses de microservices sont manquantes : " . implode(",", $diff));
    }

    foreach($conf_array as $name=>$url) {
      $this->$name = $url;
    }
  }
}

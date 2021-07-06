<?php

use \Psr\Http\Message\ServerRequestInterface as Request;
use \Psr\Http\Message\ResponseInterface as Reponse;
require 'vendor/autoload.php';

$app =  new \Slim\App
$app->get('/'function(Request $request, Reponse $response){
    $response->getBody()->write("Hello from Docker php image");
    return $response
});


$app->run();
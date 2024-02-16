"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.server = server;

/**
 * Function that provides the path of the backend URI: localhost or server depending if you are running the app locally or from the server.
 */
function server() {
  var server;
  var AppLocation;
  AppLocation = window.location.href;

  if (AppLocation.includes("localhost")) {
    //Localhost
    server = "http://127.0.0.1:4200";
  } else {
    //Server
    server = process.env.REACT_APP_BACKEND_URL;
    console.log(process.env.REACT_APP_BACKEND_URL);
  }

  return server;
}
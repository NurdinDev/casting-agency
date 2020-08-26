import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import * as serviceWorker from "./serviceWorker";
import { Auth0Provider } from "@auth0/auth0-react";
import history from "./utils/history";

const onRedirectCallback = (appState: any) => {
  history.push(
    appState && appState.returnTo ? appState.returnTo : window.location.pathname
  );
};

ReactDOM.render(
  <Auth0Provider
    domain={process.env.REACT_APP_AUTH0_DOMAIN as string}
    clientId={process.env.REACT_APP_AUTH0_CLIENT_ID as string}
    audience={"http://127.0.0.1:5000"}
    redirectUri={window.location.origin}
    onRedirectCallback={onRedirectCallback}
  >
    <App />
  </Auth0Provider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

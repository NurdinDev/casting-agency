export const API_URL =
  process.env.NODE_ENV === "production"
    ? process.env.REACT_APP_API_URL
    : "http://localhost:5000";

export const returnTo =
  process.env.NODE_ENV === "production"
    ? process.env.REACT_APP_URL
    : "http://localhost:8100";

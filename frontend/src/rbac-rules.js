const rules = {
  assistant: {
    static: ["get:movies", "get:actors"]
  },
  director: {
    static: [
      "get:actors",
      "post:actors",
      "delete:actors",
      "patch:actors",
      "patch:movies"
    ],
  },
  producer: {
    static: [
      "get:actors",
      "post:actors",
      "delete:actors",
      "patch:actors",
      "get:movies",
      "post:movies",
      "patch:movies",
      "delete:movies"
    ]
  }
};

export default rules;
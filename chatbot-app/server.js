// server.js
const express = require('express');
const bodyParser = require('body-parser');
const { chatbot } = require('./main'); // Importe a lógica do seu chatbot

const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/api/chat', (req, res) => {
  const { user_input } = req.body;

  // Adapte para suas necessidades específicas
  const chatbotResponse = chatbot(user_input);

  res.json({ response: chatbotResponse });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
    
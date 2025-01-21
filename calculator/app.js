const express = require("express");

const PORT = 3000;
const app = express();

const { spawn } = require("child_process");
const path = require("path");

app.use(express.static(path.join(__dirname)));
app.use(express.json());

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/calculate", (req, res) => {
  const { num1, num2, operation } = req.body;

  const pythonProcess = spawn("python3", ["calculator.py"]);

  pythonProcess.stdin.write(JSON.stringify({ num1, num2, operation }));
  pythonProcess.stdin.end();

  pythonProcess.stdout.on("data", (data) => {
    const result = JSON.parse(data.toString());
    res.json(result);
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`Python error: ${data}`);
    res.status(500).json({ error: "Error in calculation" });
  });
});


app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

const express = require('express');
const path = require('path');
const { generatePEE } = require('./generator');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

app.post('/api/generate', async (req, res) => {
  try {
    const buffer = await generatePEE(req.body);
    const filename = `PEE_${req.body.nombreEdificio || 'Condominio'}.docx`;
    res.setHeader('Content-Type', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
    res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
    res.send(Buffer.from(buffer));
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error generando el documento' });
  }
});

app.listen(PORT, () => {
  console.log(`PEE Generator corriendo en http://localhost:${PORT}`);
});

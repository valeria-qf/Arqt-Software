import React, { useState, useEffect } from "react";
import { Modal, Box, Typography, TextField, Button } from "@mui/material";
import axios from 'axios';


interface BasicModalProps {
  open: boolean;
  onClose: () => void;
  alunoId: number | null;
  onSave: () => void;
}

const BasicModal: React.FC<BasicModalProps> = ({ open, onClose, alunoId, onSave}) => {
  const [editedNotas, setEditedNotas] = useState({
    nota1: "",
    nota2: "",
    nota3: "",
    nota4: ""
  });

  useEffect(() => {
    const fetchAluno = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/alunos/${alunoId}/`);
        setEditedNotas({
          nota1: response.data.nota1 || "",
          nota2: response.data.nota2 || "",
          nota3: response.data.nota3 || "",
          nota4: response.data.nota4 || ""
        });
      } catch (error) {
        console.error('Erro ao buscar aluno:', error);
      }
    };

    if (open && alunoId) {
      fetchAluno();
    }
  }, [open, alunoId]);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setEditedNotas((prevNotas) => ({
      ...prevNotas,
      [name]: value
    }));
  };

  const handleSave = async () => {
    try {
      await axios.put(`http://localhost:8000/alunos/${alunoId}/`, editedNotas);
      onSave()
      onClose();
    } catch (error) {
      console.error('Erro ao salvar notas do aluno:', error);
    }
  };

  return (
    <Modal open={open} onClose={onClose}>
      <Box sx={{ position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)", width: 400, bgcolor: "background.paper", boxShadow: 24, p: 4 }}>
        <Typography variant="h6" gutterBottom>
          Editar Notas do Aluno
        </Typography>
        <TextField
          fullWidth
          label="Nota 1"
          name="nota1"
          value={editedNotas.nota1}
          onChange={handleInputChange}
          margin="normal"
        />
        <TextField
          fullWidth
          label="Nota 2"
          name="nota2"
          value={editedNotas.nota2}
          onChange={handleInputChange}
          margin="normal"
        />
        <TextField
          fullWidth
          label="Nota 3"
          name="nota3"
          value={editedNotas.nota3}
          onChange={handleInputChange}
          margin="normal"
        />
        <TextField
          fullWidth
          label="Nota 4"
          name="nota4"
          value={editedNotas.nota4}
          onChange={handleInputChange}
          margin="normal"
        />
        <Button variant="contained" onClick={handleSave} sx={{ mt: 2 }}>
          Salvar
        </Button>
      </Box>
    </Modal>
  );
};

export default BasicModal;

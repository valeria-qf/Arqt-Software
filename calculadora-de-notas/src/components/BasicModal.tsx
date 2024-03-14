import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const style = {
  position: 'absolute' as 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  boxShadow: 24,
  p: 4,
  borderRadius: 4,
};

export default function BasicModal({ open, setOpen, onClose }: { open: boolean, setOpen: React.Dispatch<React.SetStateAction<boolean>>, onClose: () => void }) {
  const handleClose = () => {
    setOpen(false);
    onClose();
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    
    handleClose();
  };

  return (
    <Modal
      open={open}
      onClose={handleClose}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      <Box sx={style}>
        <Typography id="modal-modal-title" variant="h6" component="h2">
          Adicionar Notas
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="1º Bimestre"
            type="float"
            fullWidth
            margin="normal"
          />
          <TextField
            label="2º Bimestre"
            type="float"
            fullWidth
            margin="normal"
          />
          <TextField
            label="3º Bimestre"
            type="float"
            fullWidth
            margin="normal"
          />
          <TextField
            label="4º Bimestre"
            type="float"
            fullWidth
            margin="normal"
          />
          <Box sx={{ mt: 2 }}>
            <Button type="submit" variant="contained" color="primary">
              Salvar
            </Button>
          </Box>
        </form>
      </Box>
    </Modal>
  );
}

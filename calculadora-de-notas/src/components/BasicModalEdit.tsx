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

export default function BasicModalEdit({ open, setOpen, onClose }: { open: boolean, setOpen: React.Dispatch<React.SetStateAction<boolean>>, onClose: () => void }) {
  const [firstBim, setFirstBim] = React.useState<number | ''>('');
  const [secondBim, setSecondBim] = React.useState<number | ''>('');
  const [thirdBim, setThirdBim] = React.useState<number | ''>('');
  const [fourthBim, setFourthBim] = React.useState<number | ''>('');

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
          Editar Notas
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="1º Bimestre"
            type="number"
            value={firstBim}
            onChange={(e) => setFirstBim(parseFloat(e.target.value))}
            fullWidth
            margin="normal"
            InputProps={{ inputProps: { min: 0, max: 100, step: 0.01 } }}
          />
          <TextField
            label="2º Bimestre"
            type="number"
            value={secondBim}
            onChange={(e) => setSecondBim(parseFloat(e.target.value))}
            fullWidth
            margin="normal"
            InputProps={{ inputProps: { min: 0, max: 100, step: 0.01 } }}
          />
          <TextField
            label="3º Bimestre"
            type="number"
            value={thirdBim}
            onChange={(e) => setThirdBim(parseFloat(e.target.value))}
            fullWidth
            margin="normal"
            InputProps={{ inputProps: { min: 0, max: 100, step: 0.01 } }}
          />
          <TextField
            label="4º Bimestre"
            type="number"
            value={fourthBim}
            onChange={(e) => setFourthBim(parseFloat(e.target.value))}
            fullWidth
            margin="normal"
            InputProps={{ inputProps: { min: 0, max: 100, step: 0.01 } }}
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

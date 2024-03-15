import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import InputLabel from '@mui/material/InputLabel';

interface SelectFieldProps {
  value: number;
  onChange: (event: SelectChangeEvent) => void;
}

export default function SelectField({ value, onChange }: SelectFieldProps) {
  return (
    <FormControl fullWidth margin="normal">
      <InputLabel id="select-bimestre-label">Bimestre</InputLabel>
      <Select
        labelId="select-bimestre-label"
        id="select-bimestre"
        value={value.toString()}
        onChange={onChange}
      >
        <MenuItem value={1}>1º Bimestre</MenuItem>
        <MenuItem value={2}>2º Bimestre</MenuItem>
        <MenuItem value={3}>3º Bimestre</MenuItem>
        <MenuItem value={4}>4º Bimestre</MenuItem>
      </Select>
    </FormControl>
  );
}

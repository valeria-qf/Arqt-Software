import * as React from "react";
import TextField from "@mui/material/TextField";

interface SearchProps {
  onSearch: (searchTerm: string) => void;
}

const Search: React.FC<SearchProps> = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = React.useState("");

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    onSearch(searchTerm);
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        fullWidth
        label="Buscar Aluno"
        variant="outlined"
        value={searchTerm}
        onChange={handleChange}
        margin="normal"
        sx={{ width: 900 }} 
      />
    </form>
  );
};

export default Search;

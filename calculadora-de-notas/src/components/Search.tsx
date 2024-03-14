import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';

interface SearchBarProps {
    items: { name: string; nota1: number; nota2: number; nota3: number; nota4: number; }[];
    setFilteredItems: React.Dispatch<React.SetStateAction<{ name: string; nota1: number; nota2: number; nota3: number; nota4: number; }[]>>;
}

const SearchBar: React.FC<SearchBarProps> = ({ items, setFilteredItems }) => {
  const [searchTerm, setSearchTerm] = useState<string>('');

  const handleSearch = () => {
    const filteredItems = items.filter(item =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredItems(filteredItems);
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  return (
    <div style={{ display: 'flex', width: 900}}>
      <TextField
        label="Pesquisar"
        variant="outlined"
        size="small"
        fullWidth
        value={searchTerm}
        onChange={handleChange}
      />
      <IconButton onClick={handleSearch} aria-label="search">
        <SearchIcon />
      </IconButton>
    </div>
  );
}

export default SearchBar;

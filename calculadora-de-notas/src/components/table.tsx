import * as React from "react";
import axios from 'axios';
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import EditNoteOutlinedIcon from "@mui/icons-material/EditNoteOutlined";
import IconButton from "@mui/material/IconButton";
import BasicModal from "./BasicModal"; 
import { Aluno } from "../@types/Type";
import Search from "./Search";

export default function BasicTable() {
  const [openModal, setOpenModal] = React.useState(false);
  const [selectedAlunoId, setSelectedAlunoId] = React.useState<number | null>(null);
  const [alunos, setAlunos] = React.useState<Aluno[]>([]);
  const [filteredAlunos, setFilteredAlunos] = React.useState<Aluno[]>([]);

  const fetchAlunos = async () => {
    try {
      const response = await axios.get('http://localhost:8000/alunos/');
      setAlunos(response.data);
      setFilteredAlunos(response.data); // Inicialmente, define os alunos filtrados como todos os alunos
    } catch (error) {
      console.error('Erro ao buscar alunos:', error);
    }
  };

  React.useEffect(() => {
    fetchAlunos();
  }, []);

  const handleOpenModal = (alunoId: number) => {
    setOpenModal(true);
    setSelectedAlunoId(alunoId);
  };

  const handleCloseModal = () => {
    setOpenModal(false);
    setSelectedAlunoId(null);
  };

  const handleSearch = (searchTerm: string) => {
    const filtered = alunos.filter(aluno =>
      aluno.nome.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredAlunos(filtered);
  };

  return (
    <>
      <Search onSearch={handleSearch} />

      <TableContainer component={Paper} sx={{ width: 900 }}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Alunos</TableCell>
              <TableCell align="center">Nota 1</TableCell>
              <TableCell align="center">Nota 2</TableCell>
              <TableCell align="center">Nota 3</TableCell>
              <TableCell align="center">Nota 4</TableCell>
              <TableCell align="center">Média</TableCell>
              <TableCell align="center">Action</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredAlunos.map((aluno) => (
              <TableRow
                key={aluno.id}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {aluno.nome}
                </TableCell>
                <TableCell align="center">
                  {aluno.nota1 !== null ? aluno.nota1 : '-'}
                </TableCell>
                <TableCell align="center">
                  {aluno.nota2 !== null ? aluno.nota2 : '-'}
                </TableCell>
                <TableCell align="center">
                  {aluno.nota3 !== null ? aluno.nota3 : '-'}
                </TableCell>
                <TableCell align="center">
                  {aluno.nota4 !== null ? aluno.nota4 : '-'}
                </TableCell>
                <TableCell align="center">{aluno.media !== null ? aluno.media.toFixed(2) : '-'}</TableCell>
                <TableCell
                  align="center"
                  sx={{ display: "flex", justifyContent: "center" }}
                >
                  <IconButton onClick={() => handleOpenModal(aluno.id)}>
                    <EditNoteOutlinedIcon color="primary" fontSize="medium" />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <BasicModal
        open={openModal}
        onClose={handleCloseModal}
        alunoId={selectedAlunoId}
        onSave={fetchAlunos} 
      />
    </>
  );
}

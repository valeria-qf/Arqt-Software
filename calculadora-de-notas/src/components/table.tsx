import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import AddOutlinedIcon from "@mui/icons-material/AddOutlined";
import EditNoteOutlinedIcon from "@mui/icons-material/EditNoteOutlined";
import IconButton from "@mui/material/IconButton";
import BasicModal from "./BasicModal";
import BasicModalEdit from "./BasicModalEdit";

function createData(
  name: string,
  calories: number,
  fat: number,
  carbs: number,
  protein: number
) {
  return { name, calories, fat, carbs, protein };
}

const rows = [
  createData("Frozen yoghurt", 159, 6.0, 24, 4.0),
  createData("Ice cream sandwich", 237, 9.0, 37, 4.3),
  createData("Eclair", 262, 16.0, 24, 6.0),
  createData("Cupcake", 305, 3.7, 67, 4.3),
  createData("Gingerbread", 356, 16.0, 49, 3.9),
];

export default function BasicTable() {
  const [open, setOpen] = React.useState(false);
  const [modalType, setModalType] = React.useState(""); // State to determine which modal to open

  const handleOpenModal = (type: "add" | "edit") => {
    setOpen(true);
    setModalType(type);
  };
  const handleCloseModal = () => setOpen(false);

  return (
    <>
      <TableContainer component={Paper} sx={{ width: 900 }}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Alunos</TableCell>
              <TableCell align="center">Nota 1</TableCell>
              <TableCell align="center">Nota 2</TableCell>
              <TableCell align="center">Nota 3</TableCell>
              <TableCell align="center">Nota 4</TableCell>
              <TableCell align="center">Media</TableCell>
              <TableCell align="center">Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow
                key={row.name}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell align="center">{row.calories}</TableCell>
                <TableCell align="center">{row.fat}</TableCell>
                <TableCell align="center">{row.carbs}</TableCell>
                <TableCell align="center">{row.protein}</TableCell>
                <TableCell align="center">{row.protein}</TableCell>
                <TableCell
                  align="center"
                  sx={{ display: "flex", justifyContent: "center" }}
                >
                  <IconButton onClick={() => handleOpenModal("add")}>
                    <AddOutlinedIcon color="primary" fontSize="medium" />
                  </IconButton>

                  <IconButton onClick={() => handleOpenModal("edit")}>
                    <EditNoteOutlinedIcon color="primary" fontSize="medium" />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      {modalType === "add" && (
        <BasicModal open={open} setOpen={setOpen} onClose={handleCloseModal} />
      )}

      {modalType === "edit" && (
        <BasicModalEdit open={open} setOpen={setOpen} onClose={handleCloseModal} />
      )}

    </>
  );
}

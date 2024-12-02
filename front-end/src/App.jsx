import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import TodoList from "./pages/todoList";
import AddTodo from "./pages/addTodo";
import EditTodo from "./pages/editTodo";
import Register from "./pages/register";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/todos" element={<TodoList />} />
        <Route path="/add" element={<AddTodo />} />
        <Route path="/edit/:id" element={<EditTodo />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>
  );
};

export default App;

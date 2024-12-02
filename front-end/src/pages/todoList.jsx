import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import TodoItem from "../components/todoItem";
import LogoutButton from "../components/LogoutButton"; // Importando o botão de logout

const TodoList = () => {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchTodos = async () => {
      const token = localStorage.getItem("token");
      if (!token) return;

      const response = await fetch("http://localhost:8000/api/v1/tasks/", {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();
      setTodos(data);
      setLoading(false);
    };

    fetchTodos();
  }, []);

  const handleDelete = async (id) => {
    const token = localStorage.getItem("token");

    const response = await fetch(`http://localhost:8000/api/v1/tasks/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    if (response.ok) {
      setTodos(todos.filter((todo) => todo.id !== id));
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 relative">
      <LogoutButton /> {/* Botão de logout */}
      <div className="max-w-4xl mx-auto">
        <div className="flex justify-between p-6 mb-4 rounded shadow-md bg-white">
          <h2 className="text-xl font-semibold">Tarefas</h2>
          <Link
            to="/add"
            className="py-2 px-4 bg-red-600 text-white rounded hover:bg-red-700"
          >
            Adicionar Tarefa
          </Link>
        </div>
        {loading ? (
          <div>Carregando...</div>
        ) : (
          <div>
            {todos.length === 0 ? (
              <div className="text-gray-500">Nenhuma tarefa encontrada.</div>
            ) : (
              <ul>
                {todos.map((todo) => (
                  <TodoItem
                    key={todo.id}
                    todo={todo}
                    handleDelete={handleDelete}
                  />
                ))}
              </ul>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default TodoList;

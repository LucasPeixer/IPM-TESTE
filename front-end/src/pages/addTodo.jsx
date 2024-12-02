import { useState } from "react";
import { useNavigate } from "react-router-dom";
import LogoutButton from "../components/LogoutButton";

const AddTodo = () => {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [dueDate, setDueDate] = useState("");
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    let validationErrors = {};
    // Validação de nome
    if (title.length < 3 || title.length > 100) {
      validationErrors.title = "O título deve ter entre 3 e 100 caracteres.";
    }
    // Validação de descrição
    if (description.length < 10) {
      validationErrors.description =
        "A descrição deve ter pelo menos 10 caracteres.";
    }
    // Validação de data prazo
    if (new Date(dueDate) <= new Date()) {
      validationErrors.dueDate =
        "A data de conclusão deve ser maior que a data atual.";
    }

    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }

    const token = localStorage.getItem("token");
    const response = await fetch("http://localhost:8000/api/v1/tasks", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ title, description, dueDate }),
    });

    if (response.ok) {
      navigate("/todos");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="flex justify-between items-center mb-6">
        <button
          onClick={() => navigate("/todos")}
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Voltar
        </button>
        <LogoutButton />
      </div>
      <div className="max-w-md mx-auto bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl font-semibold text-center mb-4">
          Adicionar Tarefa
        </h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="title" className="block text-sm font-medium">
              Título
            </label>
            <input
              id="title"
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
              required
            />
            {errors.title && (
              <p className="text-red-500 text-xs">{errors.title}</p>
            )}
          </div>
          <div className="mb-4">
            <label htmlFor="description" className="block text-sm font-medium">
              Descrição
            </label>
            <textarea
              id="description"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
              required
            ></textarea>
            {errors.description && (
              <p className="text-red-500 text-xs">{errors.description}</p>
            )}
          </div>
          <div className="mb-4">
            <label htmlFor="dueDate" className="block text-sm font-medium">
              Data de Conclusão
            </label>
            <input
              id="dueDate"
              type="date"
              value={dueDate}
              onChange={(e) => setDueDate(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
            />
            {errors.dueDate && (
              <p className="text-red-500 text-xs">{errors.dueDate}</p>
            )}
          </div>
          <button
            type="submit"
            className="w-full py-2 bg-red-600 text-white rounded hover:bg-red-700"
          >
            Adicionar
          </button>
        </form>
      </div>
    </div>
  );
};

export default AddTodo;

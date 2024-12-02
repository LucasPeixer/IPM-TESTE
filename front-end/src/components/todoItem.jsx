import { Link } from "react-router-dom";

const TodoItem = ({todo, handleDelete}) => {
  const isFinalized = todo.status === "Finalizado";
  return (
    <li
      key={todo.id}
      className={`mb-4 p-4 shadow-md rounded bg-white hover:bg-gray-100 ${
        isFinalized ? "opacity-50 text-gray-400" : ""
      }`}
    >
      <div className="flex justify-between items-center">
        <h3 className="font-medium">{todo.title}</h3>
        <div>
          {todo.dueDate && (
            <>
              <span className="block text-sm text-gray-500">Conclusão:</span>
              <span className="font-bold text-gray-600">
                {new Date(todo.dueDate).toLocaleDateString()}
              </span>
            </>
          )}
        </div>
      </div>
      <p>{todo.description}</p>
      <div className="flex justify-between mt-2">
        <span className="text-gray-600">{todo.status}</span>
        <div>
          <button
            onClick={() => handleDelete(todo.id)}
            className="py-1 px-3 bg-red-600 text-white rounded hover:bg-red-700"
          >
            Deletar
          </button>
          <Link
            to={`/edit/${todo.id}`}
            className="ml-2 py-1 px-3 bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            Editar
          </Link>
        </div>
      </div>
    </li>
  );
};

export default TodoItem;

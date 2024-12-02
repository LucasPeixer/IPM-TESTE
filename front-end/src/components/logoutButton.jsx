import { useNavigate } from "react-router-dom";

const LogoutButton = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <button
      onClick={handleLogout}
      className="absolute top-4 right-4 bg-red-600 text-white py-2 px-4 rounded hover:bg-red-700"
    >
      Desconectar
    </button>
  );
};

export default LogoutButton;

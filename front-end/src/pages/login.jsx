import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://localhost:8000/api/v1/users/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem("token", data.access_token);
        navigate("/todos");
      } else {
        setError(data.message || "Erro ao fazer login.");
      }
    } catch (error) {
      setError("Erro de rede. Tente novamente.");
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-full max-w-md bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl font-semibold text-center mb-4">Login</h2>
        {error && (
          <div className="bg-red-200 text-red-800 p-2 mb-4">{error}</div>
        )}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="username" className="block text-sm font-medium">
              E-mail <span className="text-red-600">*</span>
            </label>
            <input
              id="username"
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-sm font-medium">
              Senha <span className="text-red-600">*</span>
            </label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
              required
            />
          </div>
          <button
            type="submit"
            className="w-full py-2 bg-red-600 text-white rounded hover:bg-red-700"
          >
            Entrar
          </button>
        </form>
        <p className="mt-4 text-center">
          Não tem uma conta?{" "}
          <a href="/register" className="text-blue-600 hover:text-blue-800">
            Criar Conta
          </a>
        </p>
      </div>
    </div>
  );
};

export default Login;

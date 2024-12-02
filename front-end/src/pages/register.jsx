import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  //Confere email se atende o padrão
  const emailRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
  // Senha deve ter pelo menos 8 caracteres, 1 letra e 1 número
  const passwordRegex = /^(?=.*[a-zA-Z])(?=.*\d).{8,}$/;

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Validação de nome
    if (name.length < 3) {
      setError("O nome deve ter pelo menos 3 caracteres.");
      return;
    }
    // Validação de e-mail
    if (!emailRegex.test(email)) {
      setError("O e-mail não é válido.");
      return;
    }
    // Validação de senha
    if (!passwordRegex.test(password)) {
      setError(
        "A senha deve ter pelo menos 8 caracteres, incluindo 1 número e 1 letra."
      );
      return;
    }

    try {
      const response = await fetch(
        "http://localhost:8000/api/v1/users/register",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ name, email, password }),
        }
      );

      const data = await response.json();

      if (response.ok) {
        navigate("/");
      } else {
        setError(data.message || "Erro ao criar conta.");
      }
    } catch (error) {
      setError("Erro de rede. Tente novamente.");
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <div className="w-full max-w-md bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl font-semibold text-center mb-4">Criar Conta</h2>
        {error && (
          <div className="bg-red-200 text-red-800 p-2 mb-4">{error}</div>
        )}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="name" className="block text-sm font-medium">
              Nome Completo <span className="text-red-600">*</span>
            </label>
            <input
              id="name"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded mt-1"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-medium">
              E-mail <span className="text-red-600">*</span>
            </label>
            <input
              id="email"
              type="email"
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
            Criar Conta
          </button>
        </form>
        <p className="mt-4 text-center">
          Já possuí uma conta?{" "}
          <a href="/" className="text-blue-600 hover:text-blue-800">
            Entrar
          </a>
        </p>
      </div>
    </div>
  );
};

export default Register;

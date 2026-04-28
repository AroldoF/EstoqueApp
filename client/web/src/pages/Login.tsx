import { useForm } from "react-hook-form";
import { Link, useNavigate } from "react-router"; 
import { useContext } from "react"; 
import { AuthContext } from "../context/AuthContext"; 
import { api } from "../services/api"; 
import { InputField } from "../components/InputField"; 

export function Login() {
  const navigate = useNavigate();
  const { login } = useContext(AuthContext); 
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm();

  const onSubmit = async (data: any) => {
    try {
      const response = await api.post("/login", {
        email: data.email,
        password: data.password
      });

      const { token } = response.data;

     
      await login(token); 

 
      navigate("/", { replace: true }); 

    } catch (error: any) {
      const msg = error.response?.data?.detail || "E-mail ou senha incorretos";
      alert(msg);
    }
  };

  return (
   
    <div className="min-h-screen bg-[var(--color-background)] flex items-center justify-center p-4">
      <div className="bg-[var(--color-surface)] border border-[var(--color-border)] p-8 rounded-lg w-full max-w-md shadow-xl">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-[var(--color-text-primary)]">Estoque Pro</h1>
          <p className="text-[var(--color-text-secondary)] mt-2">Acesse sua conta</p>
        </div>

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
          <InputField 
            id="email" 
            type="email" 
            children="E-mail"
            placeholder="Digite seu e-mail"
            error={errors.email}
            {...register("email", { required: "E-mail obrigatório" })}
          />

          <InputField 
            id="password" 
            type="password" 
            children="Senha"
            placeholder="Sua senha secreta"
            error={errors.password}
            {...register("password", { required: "Senha obrigatória" })}
          />

          <button 
            type="submit"
            disabled={isSubmitting}
            className="w-full bg-[var(--color-primary)] hover:bg-[var(--color-primary-hover)] text-white font-bold py-3 rounded-md transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isSubmitting ? "Carregando..." : "Entrar"}
          </button>
        </form>

        <p className="text-center text-[var(--color-text-secondary)] mt-6">
          Não tem uma conta?{" "}
          <Link to="/signup" className="text-[var(--color-primary-hover)] hover:underline">
            Cadastre-se
          </Link>
        </p>
      </div>
    </div>
  );
}
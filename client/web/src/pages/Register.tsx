import { useForm } from "react-hook-form";
import { Link } from "react-router";
import { InputField } from "../components/InputField";

export function Register() {
  const { register, handleSubmit, watch, formState: { errors, isSubmitting } } = useForm();
  const password = watch("password");

  const onSubmit = (data: any) => console.log("Cadastro:", data);

  return (
    <div className="min-h-screen bg-[var(--color-background)] flex items-center justify-center p-4">
      <div className="bg-[var(--color-surface)] border border-[var(--color-border)] p-8 rounded-lg w-full max-w-md">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-[var(--color-text-primary)]">Estoque Pro</h1>
          <p className="text-[var(--color-text-secondary)] mt-2">Crie sua conta agora</p>
        </div>

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
          <InputField 
            children="Nome Completo" 
            id="name"
            {...register("name", { required: "Nome é obrigatório" })}
            error={errors.name}
          />

          <InputField 
            children="E-mail" 
            id="email" 
            type="email"
            {...register("email", { 
              required: "E-mail é obrigatório",
              pattern: { value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i, message: "E-mail inválido" }
            })}
            error={errors.email}
          />

          <InputField 
            children="Senha" 
            id="password" 
            type="password"
            {...register("password", { 
              required: "Senha é obrigatória",
              minLength: { value: 8, message: "Mínimo de 8 caracteres" },
              validate: {
                hasUpper: v => /[A-Z]/.test(v) || "Deve ter uma letra maiúscula",
                hasNumber: v => /[0-9]/.test(v) || "Deve ter um número"
              }
            })}
            error={errors.password}
          />

          <InputField 
            children="Confirmar Senha" 
            id="confirmPassword" 
            type="password"
            {...register("confirmPassword", { 
              validate: value => value === password || "As senhas não coincidem"
            })}
            error={errors.confirmPassword}
          />

          <button 
            type="submit"
            disabled={isSubmitting}
            className="w-full bg-[var(--color-primary)] hover:bg-[var(--color-primary-hover)] text-white font-bold py-3 rounded-md transition-all shadow-lg active:scale-95"
          >
            {isSubmitting ? "Criando conta..." : "Criar Conta"}
          </button>
        </form>

        <p className="text-center text-[var(--color-text-secondary)] mt-6 text-sm">
          Já possui conta?{" "}
          <Link to="/login" className="text-[var(--color-primary-hover)] hover:underline">
            Fazer login
          </Link>
        </p>
      </div>
    </div>
  );
}
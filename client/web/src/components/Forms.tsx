import { Card } from "./Card";
import { InputField } from "./InputField";
import { Button } from './Button'
import { Save } from 'lucide-react';

import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

import {api} from '../services/api'



export function Forms(){
    const navigate = useNavigate()
    const { register, handleSubmit, formState: { errors }} = useForm()

    function handleDashboard(){
        navigate('/')
    }

    async function createProduct(data){
        try{
            await api.post('/product', data)
            alert("Produto cadastrado com sucesso!")
            handleDashboard()
        }
        catch (error){
            console.log("Erro ao cadastrar o produto:", error)
            alert("Não foi possível cadastrar o produto.")
        }
    }


    return(
        <Card className={"max-w-3xl w-full mx-auto"}>
            <form className={"flex flex-col justify-center gap-9"}
            onSubmit={handleSubmit(createProduct)}>
                <div className="flex flex-col gap-3">
                    <h2 className="text-xl text-[var(--color-text-primary)]">Informações Básicas</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <InputField id="name" type="text"  placeholder="Nome do produto" 
                        className={errors?.name && "input-error"}
                        {...register("name", {required: true})}>
                            Nome do Produto *
                        </InputField>
                        {errors?.name?.type === "required" &&(
                            <span><p className="error-message">Campo obrigatório</p></span>
                        )}
                        <InputField id="sku" type="text" placeholder="SKU"
                        className={errors?.sku && "input-error"} 
                        {...register("sku", {required: true})}>
                            SKU *
                        </InputField>
                        {errors?.sku?.type === "required" &&(
                            <span><p className="error-message">Campo obrigatório</p></span>
                        )}
                    </div>
                </div>
    
                <div className="flex flex-col gap-3">
                    <h2 className="text-xl text-[var(--color-text-primary)]">Estoque e Preço</h2>
                    <div className="grid grid-cols-2 gap-4">
                        <InputField id="quantity" type="number" step="1" min="0"  placeholder="Quantidade" 
                        className={errors?.quantity && "input-error"}
                        {...register("stock", {required: true, valueAsNumber: true})}>
                            Quantidade *
                        </InputField>
                        {errors?.quantity?.type === "required" &&(
                            <span><p className="error-message">Campo obrigatório</p></span>
                        )}
                        <InputField id="price" type="number" step="0.01" placeholder="Preço"
                        className={errors?.price && "input-error"}
                        {...register("price", {required: true, valueAsNumber: true})}>
                            Preço (R$) *
                        </InputField>
                        {errors?.price?.type === "required" &&(
                            <span><p className="error-message">Campo obrigatório</p></span>
                        )}
                    </div>
                </div>
                <div className="flex flex-col gap-3">
                    <h2 className="text-xl text-[var(--color-text-primary)]">Descrição</h2>
                    <label htmlFor="description"></label>
                    <textarea id="description" placeholder="Descrição" {...register("description")}
                    className="w-full border border-[var(--color-border)] rounded-md px-3 py-2 focus:outline-none focus:border-purple-600 focus:ring-1 focus:ring-purple-600">
                    </textarea>
                </div>

                <div className="flex flex-row gap-3">
                    <label htmlFor="is_active">O produto está ativo?</label>
                    <input id="is_active" type="checkbox" 
                    {...register("is_active")}>
                    </input>
                </div>

                <div className="flex flex-row justify-end gap-4 mt-2">
                    <Button type="button" variant="secondary" text="Cancelar" onClick={handleDashboard}/>
                    <Button text="Cadastrar Produto" icon={Save} type="submit"/>
                </div>
            </form>
        </Card>
    )
}
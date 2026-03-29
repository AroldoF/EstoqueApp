import { Card } from "./Card";
import { InputField } from "./InputField";
import { Button } from './Button'
import { Save } from 'lucide-react';

import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";

import {api} from '../services/api'
import type { Product } from "../types/Product";
import { useEffect } from "react";

type Props = {
    data?: Product
    isEditing?: boolean
    productId?: number
}

export function Forms({data, isEditing = false, productId}: Props){
    const navigate = useNavigate()
    const { register, handleSubmit, reset, formState: { errors }} = useForm()

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
    function getChangedFields(original: Product | undefined, updated: any) {
    const ignoredFields = ["id", "created_at"]
    const result: any = {}

    for (const key in updated) {
        if (ignoredFields.includes(key)) continue

        if (String(updated[key]) !== String(original?.[key])) {
            result[key] = updated[key]
        }
    }

    return result
}

    async function updateProduct(formData){
    try{
        const changedData = getChangedFields(data, formData)

        if (Object.keys(changedData).length === 0) {
            alert("Nenhuma alteração feita")
            return
        }
        console.log(changedData)

        await api.patch(`/product/${productId}/`, changedData)

        alert("Produto atualizado com sucesso!")
        handleDashboard()
    }
    catch (error){
        console.log("Erro ao atualizar o produto:", error)
        alert("Não foi possível atualizar o produto.")
    }
}
    useEffect(() => {
        if (data) {
            reset(data)
        }
        }, [data, reset])


    return(
        <div className='flex flex-col gap-5'>
            <div className='h-[1px] bg-[var(--color-border)]'></div>

            <Card className={"max-w-3xl w-full mx-auto"}>
                <form className={"flex flex-col justify-center gap-9"}
                onSubmit={handleSubmit((formData) =>
  isEditing ? updateProduct(formData) : createProduct(formData)
)}>

                    <div className="flex flex-col gap-3">
                        <h2 className="text-xl text-[var(--color-text-primary)]">Informações Básicas</h2>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

                            <InputField id="name" type="text"  placeholder="Nome do produto" 
                            className={errors?.name && "input-error"}
                            error={errors?.name}
                            {...register("name", {required: "Campo obrigatório"})}>
                                Nome do Produto *
                            </InputField>

                            <InputField id="sku" type="text" placeholder="SKU"
                            className={errors?.sku && "input-error"}
                            error={errors?.sku}
                            {...register("sku", {required: "Campo obrigatório"})}>
                                SKU *
                            </InputField>

                        </div>
                    </div>
        
                    <div className="flex flex-col gap-3">
                        <h2 className="text-xl text-[var(--color-text-primary)]">Estoque e Preço</h2>
                        <div className="grid grid-cols-2 gap-4">

                            <InputField id="stock" type="number" step="1" min="0"  placeholder="Quantidade" 
                            className={errors?.stock && "input-error"}
                            error={errors?.stock}
                            {...register("stock", {required: "Campo obrigatório", valueAsNumber: true})}>
                                Quantidade *
                            </InputField>


                            <InputField id="price" type="number" step="0.01" placeholder="Preço"
                            className={errors?.price && "input-error"}
                            error={errors?.price}
                            {...register("price", {required: "Campo obrigatório", valueAsNumber: true})}>
                                Preço (R$) *
                            </InputField>

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
        </div>

    )
}
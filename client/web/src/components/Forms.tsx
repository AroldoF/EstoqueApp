import { Card } from "./Card";
import { InputField } from "./InputField";

export function Forms(){
    return(
        <Card className={"flex flex-col justify-center gap-9 max-w-3xl w-full mx-auto"}>
            <div className="flex flex-col gap-3">
                <h2 className="text-xl text-[var(--color-text-primary)]">Informações Básicas</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <InputField id="name" type="text">Nome do Produto *</InputField>
                    <InputField id="sku" type="text">SKU *</InputField>
                </div>
            </div>

            <div className="flex flex-col gap-3">
                <h2 className="text-xl text-[var(--color-text-primary)]">Estoque e Preço</h2>
                <div className="grid grid-cols-2 gap-4">
                    <InputField id="quantity" type="number" step="1" min="0">Quantidade *</InputField>
                    <InputField id="price" type="number">Preço (R$) *</InputField>
                </div>
            </div>
            <div className="flex flex-col gap-3">
                <h2 className="text-xl text-[var(--color-text-primary)]">Descrição</h2>
                <label htmlFor="description"></label>
                <textarea id="description" name="description" className="w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:border-purple-600 focus:ring-1 focus:ring-purple-600"></textarea>
            </div>
        </Card>
    )
}
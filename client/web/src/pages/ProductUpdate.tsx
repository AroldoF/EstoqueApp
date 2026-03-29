import { useState, useEffect } from "react";
import axios from "axios";
import type { Product } from "../types/Product";
import { Forms } from "../components/Forms";
import { useParams } from "react-router-dom";
import { api } from "../services/api";



// export interface Product {
//     name: string;
//     description: string;
//     stock: number;
//     price: number;
//     created_at: Date;
//     is_active: boolean;
// } 

const ProductUpdate = () => {
  const { productId } = useParams<{ productId: string }>();
  const [product, setProduct] = useState<Product | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        setLoading(true);

        const response = await api.get<Product>(`/product/${productId}`);
        
        setProduct(response.data);
      } catch (error) {
        console.error("Erro ao buscar produto:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [productId]); 
  if (loading) return <div>Carregando...</div>;
  if (!product) return <div>Produto não encontrado.</div>;

  return (
    <Forms 
    data={product}
    isEditing
    productId={Number(productId)} />
);
};

export default ProductUpdate
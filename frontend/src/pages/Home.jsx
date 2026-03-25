import React, { useEffect, useState } from "react"
import API from "../api/api"

import React, {useEffect, useState} from "react"
import API from "../api/api"
import ProductCard from "../components/ProductCard"
import React from "react";

function Home() {
  return (
    <div>
      <h1>Добро пожаловать на Stopkadr!</h1>
      <p>Здесь будут товары и видео техника</p>
    </div>
  );
}

export default Home;

function Home(){

    const [products, setProducts] = useState([])

    useEffect(()=>{

        API.get("products/")
        .then(res => setProducts(res.data))

    },[])

    return(

        <div className="container">

            <h1>Каталог товаров</h1>

            <div className="products-grid">

                {products.map(product => (

                    <ProductCard key={product.id} product={product}/>

                ))}

            </div>

        </div>

    )

}

function Home(){

    const [products, setProducts] = useState([])

    useEffect(() => {

        API.get("products/")
        .then(res => {
            setProducts(res.data)
        })

    }, [])

    return (

        <div>

        <h1>Products</h1>

        {products.map(product => (
            <div key={product.id}>
                <h3>{product.name}</h3>
                <p>{product.price}</p>
            </div>
        ))}

        </div>

    )
}

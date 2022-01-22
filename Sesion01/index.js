import express, {json} from "express";
import cors from "cors";

const app = express();
const productos = [
    {
        nombre: "Leche de almendras",
        precio: 9.5,
        estado: true,
    }
];

app.use(json());

app.use(cors()
//     {
//     methods: ["GET", "POST"],
//     origin: 'http://www.mipagina.com'
// }
);

const port = 3000;

app.get('/',(req, res)=>{
    res.status(201).json({
        message: 'Peticion realizada exitosamente',
    })
})

app.post('/producto',(req, res)=>{
    console.log(req.body);
    if (req.body) {
        productos.push(req.body);
        res.status(400).json({
            message: "Informacion incorrecta",
            producto: req.body,
        });
    }else {
        res.json({
            message: "Producto agregado exitosamente",
        });
    }
})

app.get('/productos',(req, res)=>{
    res.status(201).json({
        message: 'Losproductos son:',
        content: productos,
    })
})

app
    .route('/producto/:id')
    .get((req,res)=>{
        const {id} =req.params;
        if (productos[id-1]){
            return res.status(200).json({
                content: productos[id-1]
            });
        }else{
            return res.status(200).json({
                message: 'Producto no existe',
                content: null,
            })
        }
        // console.log(req.params);
        // res.json({
            //     message: null,
            // });
            
        })
    .put((req,res)=>{
        const {id} =req.params;
        if (productos[id-1]){
            productos[id-1] = req.body;

            return res.status(200).json({
                message: 'Producto actualizado exitosamente',
                content: productos[id-1],
            });
        }else{
            return res.status(400).json({
                message: "Producto no existe",
                content: null,
            })
        }
    })
    .delete((req,res)=>{
        const {id} =req.params;
        if (productos[id-1]){
            const producto = productos[id-1];
            productos.splice(id-1,1);

            return res.status(200).json({
                message: "Producto eliminado exitosamente",
                content: producto,
            });
        }else{
            return res.status(400).json({
                message: "Producto no existe",
                content: null,
            })
        }
    });


app.listen(port, ()=>{
    console.log(`Servicor levantado exitosamente! ${port}`)
});
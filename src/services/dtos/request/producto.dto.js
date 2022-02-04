import validator from "validator";

export function productoDto({ nombre, precio, tipoProductoId }) {

    if (validator.isEmpty(nombre)) { throw Error('El nombre del producto no puede estar vacio'); };

    if (!validator.isFloat(precio.toString())) { throw Error("El precio sólo puede contener números"); };

    if (!validator.isNumeric(tipoProductoId.toString())) { throw Error("El tipoProducto debe ser un número") };

    return { nombre, precio, tipoProductoId };

}
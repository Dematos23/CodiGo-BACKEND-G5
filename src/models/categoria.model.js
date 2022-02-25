import mongoose from "mongoose";

const categoriaSchema = new mongoose.Schema({
  nombre: {
    type: mongoose.Schema.Types.String,
    required: true,
    maxlength: 20,
    minlength: 2,
  },
  color: {
    type: mongoose.Schema.Types.String,
    default: "#000000",
    maxlength: 7,
  },
  categoriaProducto: {
    type: [mongoose.Schema.Types.ObjectId],
  },
});

export const Categoria = mongoose.model("categoria", categoriaSchema);

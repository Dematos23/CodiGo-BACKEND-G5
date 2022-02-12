import { ImagenService } from "../services/imagen.service.js";

export async function subirImagen(req, res) {
  const { id } = req.params;

  try {
    const respuesta = awaitImagenService.subirImagen(id, req.file.path);
    return res.status(200).send(respuesta);
  } catch (error) {
    return res
      .status(200)
      .json({ message: "Error al subir la imagen", content: error });
  }
}

import validator from "validator";

export function loginDto({ correo, password }) {

    if (!validator.isEmail(correo)) {
        throw Error('El correo debe ser un correo valido');
    };

    if (!validator.isStrongPassword(password)) {
        throw Error(
            "La contraseña no es suficientemente segura, debe tener al menos una Mayus, una minus, un número, un símbolo y una longitud mínima de 8 caracteres"
        );
    };

    return { correo, password };

}
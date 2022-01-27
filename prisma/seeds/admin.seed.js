export default async (prisma) => {
    await prisma.usuario.upsert({
        create: {
            nombre: 'Diego',
            correo: 'dematos23@gmail.com',
            password: '123456',
            tipoUsuario: 'ADMIN',
        },
        update: {},
        where: {
            correo: "dematos23@gmail.com",
        },
    })
}
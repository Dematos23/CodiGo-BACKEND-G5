import Prisma from '@prisma/Client'
const { PrismaClient } = Prisma;

export const prisma = new PrismaClient();
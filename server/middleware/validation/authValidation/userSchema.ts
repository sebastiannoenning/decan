import joiBase from 'joi'
import joiDate from '@joi/date'
const joi = joiBase.extend(joiDate) as typeof joiBase;

export const userSchema = {
  createUser: joi.object({
    username: joi.string().min(6).max(32).required(),
    password: joi.string().min(8).max(64).required(),
    passwordConfirmation: joi.string().required().valid(joi.ref('password')),
    userProfile: joi.object({
      forename: joi.string().min(1).max(35).required(),
      surname: joi.string().max(50).optional(),
      dateofbirth: joi.date().iso().less('now').min('1-1-1900').required(),
      photo: joi.string().label('Image upload').optional(),
      address: joi.number().max(10).optional()
    }),
  }),
  loginUser: joi.object({
    username: joi.string().min(6).max(32).required(),
    password: joi.string().min(8).max(64).required()
  }),
  updateUser: joi.object({
    userID: joi.number().max(3),
    username: joi.string().min(6).max(32),
    forename: joi.string().min(1).max(35),
    surname: joi.string().max(50),
    dateofbirth: joi.date().iso().less('now').min('1-1-1900'),
    photo: joi.string().label('Image upload'),
    address: joi.number().max(10)
  }),
  updatePassword: joi.object({
    userId: joi.number().max(3),
    password: joi.string().min(8).max(64).required(),
    passwordConfirmation: joi.string().required().valid(joi.ref('password'))
  })
}
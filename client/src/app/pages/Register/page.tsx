
import Navbar from '@/app/components/navbar'
import RegisterPage from '@/app/components/register'
import React from 'react'

type Props = {}

export default function register({}: Props) {
  return (
    <div>
      <Navbar></Navbar>
      <RegisterPage></RegisterPage>
    </div>
  )
}


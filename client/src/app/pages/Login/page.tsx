import LoginPage from '@/app/components/login'
import Navbar from '@/app/components/navbar'
import React from 'react'

type Props = {}

export default function page({}: Props) {
  return (
    <div>
        <Navbar></Navbar>
        <LoginPage></LoginPage>
    </div>
  )
}
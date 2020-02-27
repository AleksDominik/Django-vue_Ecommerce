import Vue from 'vue'
import Router from 'vue-router'
import Home from  '../views/Home.vue'
import About from '../views/About.vue'
import toastr from '../components/shared/service/ErrorHandler'

import {
  isLoggedIn
} from '../components/shared/service/authService'

Vue.use(Router)

function lazyLoad(view){
  return() => import(`@/views/${view}.vue`)
}

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [{
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: About
  },
  {
    path: '/products',
    name: 'products',
    component: lazyLoad('Products')
  },
  {
    path: '/products/:id',
    name: 'productDetails',
    component: () => import('../components/products/ProductDetail.vue')
  },
  {
    path: '/cart',
    name: 'cart',
    component: () => import('../components/products/cart/CartProducts.vue'),
    beforeEnter: (to, from, next) => {
      if (isLoggedIn()) {
        next()
      } else {
        next({
          name: 'login',
          query: {
            from: to.name
          }
        })
      }
    }
  },
  {
    path: '/checkout',
    name: 'checkout',
    component: () => import('../components/products/cart/Checkout.vue'),
    beforeEnter: (to, from, next) => {
      if (isLoggedIn()) {
        next()
      } else {
        next({
          name: 'login',
          query: {
            from: to.name
          }
        })
      }
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/login.vue')
  }
   ]
}
)

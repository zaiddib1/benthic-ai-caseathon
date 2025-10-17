const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/HomePage.vue') },
      { path: '/solution', component: () => import('pages/SolutionPage.vue') },
      { path: '/game', component: () => import('pages/GamePage.vue') },
      { path: '/about', component: () => import('pages/AboutPage.vue') },
      { path: '/dataset', component: () => import('pages/DatasetPage.vue') }
    ]
  },  

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes

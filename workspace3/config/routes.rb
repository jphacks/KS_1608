Rails.application.routes.draw do
  get 'sessions/new'

  root 'static_pages#home'
  get 'list' => 'lists#show'
  post 'list' => 'lists#create'
  get 'about' => 'static_pages#about'
  get 'signup' => 'users#new'
  get 'login' => 'sessions#new'
  post 'login' => 'sessions#create'
  delete 'logout' => 'sessions#destroy'
  resources :users
end

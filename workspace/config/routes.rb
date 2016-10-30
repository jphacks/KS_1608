Rails.application.routes.draw do
  root 'static_pages#home'
  get 'list' => 'static_pages#list'
  get 'signup' => 'users#new'
end

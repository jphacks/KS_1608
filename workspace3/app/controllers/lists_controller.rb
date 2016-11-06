class ListsController < ApplicationController
    def show
        @user = User.find(session[:user_id])
        # @mymessage = "Hello!"
        @botmessage = "Hello, " + @user.name
    end
    
    def create
        @mymessage = params[:list][:message]
        # print @mymessage
        render 'show'
    end
end

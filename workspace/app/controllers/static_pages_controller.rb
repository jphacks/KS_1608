class StaticPagesController < ApplicationController
  def home
    if params[:message]
      @message = params[:message]
    end
  end

  def list
  end
end

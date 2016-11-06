require 'test_helper'

class StaticPagesControllerTest < ActionController::TestCase
  def setup
    @base_title = "MONOCLE"
  end
  test "should get home" do
    get :home
    assert_response :success
    assert_select "title", "#{@base_title}" # <title>タグ内に"Home | MONOCLE"があるかチェック
  end
  
  test "should get about" do
    get :about
    assert_response :success
    assert_select "title", "About | #{@base_title}" # <title>タグ内に"About | MONOCLE"があるかチェック
  end

end

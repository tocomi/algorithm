N, K = gets.split.map(&:to_i)
S = gets

stack = []
answer = []
S.each_char.each_with_index do |char, index|
  stack.push(index) if char == '('
  answer = [stack.pop + 1, index + 1] if char == ')'

  if answer[0] == K then
    p(answer[1]);exit if answer[0] == K
    exit
  elsif answer[1] == K then
    p(answer[0])
    exit
  end
end

input = gets
ans = -1

input.each_char.each_with_index do |char, index|
  next unless char == 'c'

  cww_idx = []
  cww_idx.push(index)

  input.each_char.each_with_index do |inner_char, inner_index|
    next unless inner_index > index && inner_char == 'w'
    cww_idx.push(inner_index)
    break if cww_idx.length >= 3
  end

  break if cww_idx.length < 3

  if (ans == -1 || ans > (cww_idx.last - cww_idx.first) + 1) then
    ans = (cww_idx.last - cww_idx.first) + 1
  end
end

p(ans)

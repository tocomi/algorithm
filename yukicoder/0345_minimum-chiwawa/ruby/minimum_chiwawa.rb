input = gets
cww_idx = []
ans = -1

input.each_char.each_with_index do |char, index|
  next unless char == 'c'

  cww_idx.push(index)
  input.each_char.each_with_index do |inner_char, inner_index|
    next if inner_index <= index
    cww_idx.push(inner_index) if inner_char == 'w'
    break if cww_idx.length >= 3
  end

  break if cww_idx.length < 3

  if (ans == -1 || ans > (cww_idx.last - cww_idx.first) + 1) then
    ans = (cww_idx.last - cww_idx.first) + 1
    cww_idx = []
  end
end

p(ans)

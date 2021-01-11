$(document).ready(()=>{
    let search = document.getElementById('search')

    $(function () {
        $('[data-toggle="popover"]').popover()
      })
  
  $('.home-route').click(()=>{
    $('.home-route').removeClass('default')
    $('.home-route').addClass('selected')
    $('.search-route').addClass('default')
    $('.disco-route').addClass('default')
    $('.search-route').removeClass('selected')
    $('.disco-route').removeClass('selected')
    window.location.href = '/'
  })
  
  $('.search-route').click(()=>{
    $('.search-route').removeClass('default')
    $('.search-route').addClass('selected')
    $('.home-route').addClass('default')
    $('.disco-route').addClass('default')
    $('.home-route').removeClass('selected')
    $('.disco-route').removeClass('selected')
    
  })

  $('.disco-route').click(()=>{
    $('.disco-route').removeClass('default')
    $('.disco-route').addClass('selected')
    $('.home-route').addClass('default')
    $('.search-route').addClass('default')
    $('.home-route').removeClass('selected')
    $('.search-route').removeClass('selected')
    window.location.href = '/discover'
  })

  if (window.location.pathname == '/'){
    $('.home-route').addClass('selected')
  }else if (window.location.pathname == '/discover'){
    $('.disco-route').addClass('selected')
  }


  let share = document.getElementById('share-btn')
  let copy_text = document.getElementById('copy_text')

  if (share){
    share.addEventListener('click', ()=>{
      to_copy = share.getAttribute('data-link')
      copy_text.select()
      copy_text.setSelectionRange(0, 99999)
      document.execCommand('copy')
      console.log(copy_text)
    })
  }
  
})
import { Component, OnInit } from '@angular/core';
import { Category } from 'src/app/models/category.model';
import { CategoryService } from 'src/app/services/my-app.service';

@Component({
  selector: 'app-add-category',
  templateUrl: './add-category.component.html',
  styleUrls: ['./add-category.component.css']
})
export class AddCategoryComponent implements OnInit {

  category: Category = {
    name: '',
    ordering: 1
  };
  submitted = false;

  constructor(private categoryService: CategoryService) { }

  ngOnInit(): void {
  }

  saveCategory(): void {
    const data = {
      name: this.category.name,
      ordering: this.category.ordering
    };

    this.categoryService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
        });
  }
  newCategory(): void {
    this.submitted = false;
    this.category = {
      name: '',
      ordering: 1
    };
  }
}
